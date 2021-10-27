import math
import numpy as np

def dcm_resize_crop(dicom,new_size):
  #this will take the given file, assumed to be a dicom and will downsize and square it to the give dimension of new_size,new_size. This causes a center crop
  #resizing of DICOMs encounters issues if it new size is more than 14 times smaller than original. to overcome this any resizing that is would reduce the original by a factore of more than 14 is split into 2 or more stages, through recursion
  if dicom.Rows/new_size>=14 or dicom.Cols/new_size >=14:
      dcm_resize_crop(dicom,math.floor(new_size/2))
  row_div= math.floor(dicom.Rows/new_size)
  col_div= math.floor(dicom.Columns/new_size)
  row_left_crop = math.ceil((dicom.Rows%row_div)/2)
  col_top_crop = math.ceil((dicom.Columns%col_div)/2)

  dicom.PixelData= dicom.pixel_array[::row_div,::col_div][row_left_crop:row_left_crop+new_size,col_top_crop:col_top_crop+new_size].tobytes()

  dicom.Rows =dicom.Columns = new_size

  return dicom

def dcm_flip(dicom):

    dicom.PixelData = np.fliplr(dicom.pixel_array).tobytes()

    return dicom

def dcm_rotate(dicom, num_of_rot90):

    # copy the data back to the original data set
    dicom.PixelData = np.rot90(dicom,k=num_of_rot90).tobytes()

    if num_of_rot90%2:
        newshape = (dicom.Columns, dicom.Rows)
        dicom.Rows= newshape[0]
        dicom.Columns = newshape[1]
    return dicom
