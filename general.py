import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('creating directory'+ directory)
        os.makedirs(directory)


def create_data_files(project_name, base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    dead_link = project_name + '/dead.txt'
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')
    if not os.path.isfile(dead_link):
        write_file(dead_link,'')


def write_file(path , data):
    f =open(path,'w')
    f.write(data)  
    f.close()

# create_data_files('linkChecker', 'https://www.youtube.com')

#add data to the existing file
def append_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

def delete_data(path):
        open(path, 'w').close()
        


#saving data in the set to make crawling faster and removing duplicacy

def file_to_set(file_name):
    result= set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n',''))
    return result

def set_to_file(links, file):
    delete_data(file)
    for link in  sorted(links):
        append_file(file, link)
