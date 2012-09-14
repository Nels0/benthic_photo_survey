from photo_tagging import *
import osr

class bps_shp_exporter(object):
    def __init__(self, file_path, overwrite=True,lyr_name='bps_points',epsg_in=CONF_INPUT_EPSG,epsg_out=CONF_OUTPUT_EPSG):
        self.overwrite = overwrite
        self.file_path = self.__validate_fp(file_path)
        #-----Set up the shapefile-------------------------
        self.spatialRefIn = osr.SpatialReference()
        self.spatialRefIn.ImportFromEPSG(epsg_in)
        # if epsg_out is None, we want to output in the epsg_in spatial reference
        if epsg_out:
            self.spatialRefOut = osr.SpatialReference()
            self.spatialRefOut.ImportFromEPSG(epsg_out)
            self.sr_trans = osr.CoordinateTransformation(self.spatialRefIn,self.spatialRefOut)
        else:
            self.spatialRefOut = self.spatialRefIn
            self.sr_trans = None
        self.driver = ogr.GetDriverByName('ESRI Shapefile')
        self.ds = self.driver.CreateDataSource(self.file_path)
        self.lyr = self.ds.CreateLayer(lyr_name, self.spatialRefOut, ogr.wkbPoint)
        self.f_dict = { 'date_loc'  : ogr.OFTString,
                        'date_utc'  : ogr.OFTString,
                        'time_loc'  : ogr.OFTString,
                        'time_utc'  : ogr.OFTString,
                        'img_path'  : ogr.OFTString,
                        'direction' : ogr.OFTReal,
                        'depth'     : ogr.OFTReal,
                        'temp'      : ogr.OFTReal,
                        'habitat'   : ogr.OFTString,
                        'subst'     : ogr.OFTString, }
        for k,v in self.f_dict.iteritems():
            new_field = ogr.FieldDefn(k, v)
            if k == 'img_path':
                new_field.SetWidth(100)
            self.lyr.CreateField(new_field)
        
        self.lyrDefn = self.lyr.GetLayerDefn()
        self.feat_index = 0
        
    def __validate_fp(self, file_path):
        """
        Validate a file path.
        """
        if os.path.basename(file_path).lower().endswith('.shp'):
            if os.path.exists(file_path):
                if self.overwrite:
                    os.remove(file_path)
                    return file_path
                else:
                    raise ValueError('That shapefile already exists and the bps_shp_exporter is not set to overwrite files.')
                    return None
            else:
                return file_path
        else:
            raise ValueError('That is not a shapefile.')
            return None
    
    def add_point_from_image(self, imf):
        """
        Take an image_file object (defined in photo_tagging.py) and make a 
        shapefile feature out of it.
        """
        if imf.position:
            feat = ogr.Feature(self.lyrDefn)
            geom = imf.position.ogr_point
            geom.AssignSpatialReference(self.spatialRefIn)
            if self.sr_trans:
                geom.Transform(self.sr_trans)
            feat.SetGeometry(geom)
            feat.SetFID(self.feat_index)
            feat.SetField( 'date_loc', imf.datetime.strftime('%d/%m/%Y') )
            feat.SetField( 'date_utc', imf.utc_datetime.strftime('%d/%m/%Y') )
            feat.SetField( 'time_loc', imf.datetime.strftime('%H:%M:%S') )
            feat.SetField( 'time_utc', imf.utc_datetime.strftime('%H:%M:%S') )
            feat.SetField( 'img_path', str(imf.file_path) )
            if imf.exif_direction:
                feat.SetField( 'direction', imf.exif_direction )
            if imf.exif_depth:
                feat.SetField( 'depth', imf.exif_depth )
            if imf.xmp_temperature:
                feat.SetField( 'temp', imf.xmp_temperature )
            if imf.xmp_habitat:
                feat.SetField( 'habitat', imf.xmp_habitat )
            if imf.xmp_substrate:
                feat.SetField( 'subst', imf.xmp_substrate )
            self.lyr.CreateFeature(feat)
            feat.Destroy()
            self.feat_index += 1
            
    def write_prj(self):
        # create the *.prj file
        outSpatialRef = self.spatialRefOut
        outSpatialRef.MorphToESRI()
        prj_fname = self.file_path[:-3] + 'prj'
        f = open(prj_fname, 'w')
        f.write(outSpatialRef.ExportToWkt())
        f.close()
        
    def write_shapefile(self, image_dir):
        """
        Create a shapefile from a directory of tagged jpeg images.
        """
        file_paths = [ os.path.join(image_dir,fp) for fp in os.listdir(image_dir) if fp.lower().endswith('.jpg') ]
        for fp in file_paths:
            imf = image_file( fp )
            self.add_point_from_image( imf )
        self.write_prj()
        self.ds.Destroy() # This makes the driver actually write out the shapefile
        return self.file_path
    
    
    
    
