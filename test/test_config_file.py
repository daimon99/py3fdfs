# coding: utf-8
CONF_FILE = '~/.local/etc/fdfs/client.conf'


def test_use_storage_id():
    from fdfs_client import client
    client.get_tracker_conf(CONF_FILE)


def test_upload():
    from fdfs_client import client
    cli = client.Fdfs_client(client.get_tracker_conf(CONF_FILE))
    ret = cli.upload_appender_by_buffer(b'a', 'test')
    remote_file_id = ret['Remote file_id']
    cli.delete_file(remote_file_id)


def test_create_appender_by_zefo_buffer():
    from fdfs_client import client
    cli = client.Fdfs_client(client.get_tracker_conf(CONF_FILE))
    ret = cli.upload_appender_by_buffer(b'', 'test')
    remote_file_id = ret['Remote file_id']
    cli.delete_file(remote_file_id)



def test_get_file_info():
    import struct
    import socket
    global sock
    sock = socket.create_connection(('192.168.50.39', 22122))
    from fdfs_client import fdfs_protol
    fmt_header = '!Q B B'
    cmd = fdfs_protol.STORAGE_PROTO_CMD_QUERY_FILE_INFO
    status = 0

    # @group_name: 16byte str
    # filename: 文件名
    # 响应
    # @file_size: 8byte
    # create_timestamp: 8byte int
    # @crc32: 8byte int
    # @source_ip_addr: 16byte str
    remote_file_id = b'M00/00/1D/oYYBAF7909iEOpliAAAAAIYyvKw3935.gz'
    group_name = b'group1'

    fmt_body = '!16s %ds' % len(remote_file_id)
    body = struct.pack(fmt_body, group_name, remote_file_id)

    head = struct.pack(fmt_header, len(body), cmd, status)

    print(head)
    print(body)
    sock.sendall(head)
    sock.sendall(body)

    ret = sock.recv(1024)
    print(ret)
