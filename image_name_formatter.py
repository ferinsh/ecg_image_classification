import os
import pandas as pd

image_path = 'data/ptb-xl_images_multiprocessed'


filenames = []
for i, filename in enumerate(os.listdir(image_path)):
    filenames.append(filename.split('_')[1].split('.')[0])
df = pd.DataFrame({'filename': filenames})
unique_names = df['filename'].unique()
print(unique_names)
for name in unique_names:
    shape = df[df['filename'] == name].shape
    if shape[0] > 1000:
        print(f"{name}: ", shape)

mi_ischemia_labels = [
    'AMI', 'IMI', 'PMI', 'LMI', 'ALMI', 'ASMI', 'ILMI', 'IPMI', 'IPLMI',
    'ISC', 'ISCAL', 'ISCAN', 'ISCIL', 'ISCLA', 'ISCIN', 'ISCAS',
    'INJAS', 'INJAL', 'INJIL', 'INJLA', 'INJIN'
]

conduction_labels = [
    '1AVB', '2AVB', '3AVB',
    'CRBBB', 'IRBBB', 'CLBBB', 'ILBBB',
    'LAFB', 'LPFB', 'IVCD'
]

arrhythmia_labels = [
    'AFIB', 'AFLT', 'PSVT',
    'PAC', 'PVC',
    'SVARR', 'SARRH',
    'SBRAD', 'WPW', 'PACE', 'SR'
]

hypertrophy_labels = [
    'LVH', 'RVH',
    'LAO-LAE', 'RAO-RAE'
]

morphology_labels = [
    'INVT', 'LOWT', 'NDT',
    'HVOLT', 'LVOLT', 'LNGQT',
    'PRC(S)', 'ABQRS', 'LPR', 'QWAVE'
]

other_labels = [
    'ANEUR', 'DIG', 'SEHYP', 'BIGU', 'EL'
]

normal_labels = ['NORM']
