def dcm_resize_crop(dicom,new_size):
  #this will take the given file, assumed to be a dicom and will downsize and square it to the give dimension of new_size,new_size. This causes a center crop

  row_div= math.floor(dicom.Rows/new_size)
  col_div= math.floor(dicom.Columns/new_size)
  row_left_crop = math.ceil((dicom.Rows%row_div)/2)
  col_top_crop = math.ceil((dicom.Columns%col_div)/2)

  dicom.PixelData= dicom.pixel_array[::row_div,::col_div][col_right_crop:col_right_crop+new_size,row_right_crop:row_right_crop+new_size].tobytes()

  dicom.Rows =dicom.Columns = new_size

  return dicom

def dcm_flip(dicom):

    dicom.PixelData = np.fliplr(dicom.pixel_array).tobytes()
    ds.save_as('DICOMS/Dataset_NN/FRTest/F_'+new_filename)
    return dicom

def dcm_rotate(dicom, num_of_rot90):

    # copy the data back to the original data set
    dicom.PixelData = np.rot90(dicom,k=num_of_rot90).tobytes()

    if num_of_rot90%2:
        newshape = (dicom.Columns, dicom.Rows)
        dicom.Rows= newshape[0]
        dicom.Columns = newshape[1]
    return dicom
