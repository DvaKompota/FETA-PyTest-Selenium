from resources.utils import file_ops
from os.path import join


relative_path_from_here_to_yaml = join('data.yaml')
feta_data = file_ops.get_yaml(__file__, relative_path_from_here_to_yaml)
