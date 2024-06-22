from console import Console


if __name__ == '__main__':
    console = Console()

    try:
        console.run()
    except (Exception, KeyboardInterrupt) as error:
        print('ERROR', type(error).__name__, error)
        console.server_stop()
