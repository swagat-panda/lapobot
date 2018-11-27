import json
with open('Filelist.json', 'r') as f:
	dic_file_list = json.load(f)
with open(dic_file_list['filelist']['database_config_file'], 'r') as f:
	dic_database_config = json.load(f)

print(dic_database_config['dbclient']['dbconn'])