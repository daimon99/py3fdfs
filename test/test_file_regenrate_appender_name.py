# coding: utf-8

storage_server = 'fdfs_server'


def test_regenerate_appender_file_name():
    from fdfs_client import client
    cli = client.Fdfs_client(client.get_tracker_conf('~/.local/etc/fdfs/client.conf'))
    ret = cli.upload_appender_by_buffer(b'just a test', 'test')
    file_id = ret.get('Remote file_id')
    try:
        print(file_id)
        ret = cli.regenerate_appender_filename(file_id)
        print('regenerate appender filename: ', ret)
    except:
        raise
    finally:
        ret = cli.delete_file(ret.get('Remote file_id'))
        print('delete result', ret)
