# Abstração
# Herança - é um
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
          raise NotImplementedError('Impletemente o método log')
    
    def log_error(self, msg):
         return self._log(f'Error: {msg}')

    def log_success(self, msg):
         return self._log(f'Success: {msg}')

    
class LogFileMixin(Log):
     def  _log(self, msg):
          msg_formatada = f'{msg} ({self.__class__.__name__})'
          print(f'Salvando no log: {msg}')
          with open(LOG_FILE, 'a') as arquivo:
               arquivo.write(msg_formatada)
               arquivo.write('\n')

class LogPrintMixin(Log):
     def  _log(self, msg):
          print(f'{msg} ({self.__class__.__name__})')

if __name__ ==  '__main__':
    lp = LogPrintMixin()
    lp.log_error('Deu ruim zé!')
    lp.log_success('Deu bom!')
    lf = LogFileMixin()
    lf.log_error('Deu ruim zé!')
    lf.log_success('Deu bom!')    