from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _parmed_Structure : form_name
}

