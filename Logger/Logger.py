from enum import Enum
from print_color import print
import inspect
from dataclasses import dataclass
import platform


class Logger:
    if platform.system() == 'Windows':
        class Type(Enum):
            ERROR = '❌'
            WARNING = '⚠️'
            INFO = '📫'
            SUCCESS = '✔️'
    else:
        class Type(Enum):
            ERROR = '❌'
            WARNING = '🟨'
            INFO = '📫'
            SUCCESS = '✅'

    @dataclass
    class Err:
        exception: Exception
        msg: str

    @staticmethod
    def log(log_type: Type, area: str, message: str, **kwargs) -> None:

        if log_type == Logger.Type.ERROR:
            Logger.error(area, message, loc=kwargs.get('loc'))

        if log_type == Logger.Type.INFO:
            Logger.info(area, message, loc=kwargs.get('loc'))

        if log_type == Logger.Type.SUCCESS:
            Logger.success(area, message, loc=kwargs.get('loc'))

        if log_type == Logger.Type.WARNING:
            Logger.warning(area, message, loc=kwargs.get('loc'))

    @staticmethod
    def error(area: str, message: str, error: Err = Err(Exception,  ''), **kwargs) -> None:

        final = f'{Logger.Type.ERROR.value}  {message}'

        if loc := kwargs.get('loc'):
            final += f', Ln:{loc} '

        print(final, tag=f'{area}',
              tag_color='white', background='black',  format='bold')
        print()

        raise error.exception(error.msg)

    @staticmethod
    def success(area: str, message: str, **kwargs) -> None:
        final = f'{Logger.Type.WARNING.SUCCESS.value}  {message}'

        if loc := kwargs.get('loc'):
            final += f', Ln:{loc} '

        print(final, tag=f'{area}',
              tag_color='white', background='black',  format='bold', color='white')
        print()

    @staticmethod
    def info(area: str, message: str, **kwargs) -> None:

        final = f'{Logger.Type.WARNING.INFO.value} {message}'

        if loc := kwargs.get('loc'):
            final += f', Ln:{loc} '

        print(final, tag=f'{area}',
              tag_color='white', background='black',  format='bold')
        print()

    @staticmethod
    def warning(area: str, message: str, **kwargs) -> None:
        final = f'{Logger.Type.WARNING.value}  {message}'

        if loc := kwargs.get('loc'):
            final += f', Ln:{loc} '

        print(final, tag=f'{area}',
              tag_color='white', background='black', format='bold', color='white')
        print()

    @staticmethod
    def line():
        return inspect.currentframe().f_back.f_lineno

    @staticmethod
    def operation(name: str, result: any, expected_result: any, **kwargs):

        final = f'{name}: Expected Value: {expected_result} | Real Value: {result}'

        if result == expected_result:
            Logger.success(name, final, loc=kwargs.get('loc'))
        else:
            Logger.warning(name, final, loc=kwargs.get('loc'))

    @staticmethod
    def debug(name: str, result: any, expected_result: any, error: Err, **kwargs):

        final = f'{name}: Expected Value: {expected_result} | Real Value: {result}'

        if result == expected_result:
            Logger.success(name, final, loc=kwargs.get('loc'))
        else:
            Logger.error(name, final, error, loc=kwargs.get('loc'))



Logger.debug(name='Sum', result=2+2, expected_result=4,         
    error=Logger.Err(ValueError, 'msg'))