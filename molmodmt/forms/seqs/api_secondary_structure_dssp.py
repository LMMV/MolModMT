from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].replace('api_','')+':seq'

is_form={
    'secondary_structure_dssp:seq' : form_name
}

_dssp_to_abc = {"I" : "c", # coil
                "S" : "c",
                "H" : "a", # helix
                "E" : "b", # sheet
                "G" : "c",
                "B" : "b",
                "T" : "c",
                "C" : "c",
                "X" : "X"} # undefined

def to_secondary_structure_abc(item):
    pass

def get_shape(item):
    raise NotImplementedError

def select_with_mdtraj(item, selection):
    raise NotImplementedError

def extract_atom_indices(item, atom_indices):
    raise NotImplementedError
