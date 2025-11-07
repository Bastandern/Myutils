import click
from pathlib import Path
from . import file_tools
from . import web_tools

@click.group()
def cli():
    """
    MyUtils: 你的个人多功能CLI工具箱
    """
    pass

@cli.command()
def hello():
    click.echo("Hello, World! 你的 MyUtils 工具正在工作!")

@cli.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--algorithm', '-a', default='sha256', help='哈希算法 (md5, sha1, sha256...)')
def hash(file, algorithm):
    file_path = Path(file)
    result = file_tools.calculate_hash(file_path, algorithm)
    click.echo(result)

@cli.command()
@click.argument('path', type=click.Path(exists=True), default='.')
@click.option('--depth', '-d', default=2, type=int, help='显示的目录深度')
def tree(path, depth):
    dir_path = Path(path)
    file_tools.list_tree(dir_path, max_depth=depth)

@cli.command()
@click.argument('ip_address')
def ip(ip_address):
    info = web_tools.get_ip_info(ip_address)
    if info.get('status') == 'success':
        click.echo(f"--- IP {info['query']} 的信息 ---")
        click.echo(f"  国家: {info.get('country')}")
        click.echo(f"  城市: {info.get('regionName')}, {info.get('city')}")
        click.echo(f"  ISP : {info.get('isp')}")
    else:
        click.echo(f"查询失败: {info.get('message')}")
if __name__ == '__main__':
    cli()