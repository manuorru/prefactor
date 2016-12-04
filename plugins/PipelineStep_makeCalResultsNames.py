import os
from lofarpipe.support.data_map import DataMap
from lofarpipe.support.data_map import DataProduct


def plugin_main(args, **kwargs):
    """
    create the name for the results directory of a calibrator pipeline

    Parameters
    ----------
    mapfile_in : str
        Filename of datamap with the input files
    extension : str
        extension to add to the output-names
    mapfile_dir : str
        Directory in which to put the created mapfiles

    Returns
    -------
    result : dict
        New datamap filename

    """
    mapfile_in = kwargs['mapfile_in']
    extension = kwargs['extension']
    mapfile_dir = kwargs['mapfile_dir']

    map_in = DataMap.load(mapfile_in)

    observation_list = []
    for i, item in enumerate(map_in):
        obs_name = item.file.split("_")[0]
        if not obs_name in observation_list:
            observation_list.append(obs_name)
    observation_list.sort()
    
    newname = ""
    for obsname in observation_list:
        newname += obsname+"_"
    newname += extension

    map_out = DataMap([])
    map_out.data.append(DataProduct("localhosdt", newname, False))

    fileid = os.path.join(mapfile_dir, "makeCalResultsDirname.mapfile")
    map_out.save(fileid)
    result = {'dirname': fileid}

    return result
