from server import Server
from typing import Optional, Iterable


class Console:
    def __init__(self) -> None:
        self._server: Server = Server()
        self._COMMANDS: dict[str, function] = {
            'help': self.help,
            'quit': self.exit,
            'exit': self.exit,
            'start': self.server_start,
            'stop': self.server_stop,
            'status': self.server_status
        }
        self._COMMANDS_HELP: dict[str, str] = {
            'help': 'display inforamation about commands',
            'quit': 'exit from console',
            'exit': 'exit from console',
            'start': 'start server',
            'stop': 'stop server',
            'status': 'get status of server'
        }
        self._is_run: bool = False
        self._prefix_input: str = '>>> '


    def run(self) -> None:
        self._is_run = True
        while self._is_run:
            user_input = input(self._prefix_input)
            command: Optional[function] = self._COMMANDS.get(user_input)
            if command is None:
                print(f'Unknown command: {user_input}')
            else:
                command()


    def help(self) -> None:
        unknow_commands = []
        for command_name in self._COMMANDS:
            help_message = self._COMMANDS_HELP.get(command_name)
            if help_message:
                print(f'{command_name} — {help_message}')
            else:
                unknow_commands.append(command_name)
        
        if unknow_commands:
            print('Unknow commands:', *unknow_commands)


    def exit(self) -> None:
        if self._server.is_run():
            self._server.stop()
            print('Server was stopped')
        self._is_run = False


    def server_start(self) -> None:
        if self._server.is_run():
            print('Server already was started')
        else:
            self._server.run()
            print(f'Server was started on address: {self._server.get_address()}')


    def server_stop(self) -> None:
        if self._server.is_run():
            self._server.stop()
            print('Server was stopped')
        else:
            print('Server already was stopped')


    def server_status(self) -> None:
        if self._server.is_run():
            print(f'Server is ON')
        else:
            print(f'Server is OFF')
