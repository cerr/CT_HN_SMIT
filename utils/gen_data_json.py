import os, json, sys
from glob import glob

data_dir = sys.argv[1]
nii_filelist = glob(os.path.join(data_dir,'*.nii*'))

out_json = os.path.join(data_dir,'data.json')

data_json = {'val':[]}

for nii_file in nii_filelist:
    nii_base = os.path.basename(nii_file)
    data_json['val'].append({'image':nii_base})

json_object = json.dumps(data_json, indent=4)
 
# Writing to sample.json
with open(out_json, "w") as outfile:
    outfile.write(json_object)
