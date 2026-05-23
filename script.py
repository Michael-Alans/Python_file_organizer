import os
import shutil

source_dir = '.'
target_dir = os.path.join('.', 'PDF Documents')

if not os.path.exists(target_dir):
    os.makedirs(target_dir) 

for filename in os.listdir(source_dir):
    if filename.endswith('.pdf'):
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        shutil.move(source_file, target_file)
        print(f'Moved: {filename}')