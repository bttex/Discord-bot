Discord Bot para Agendamento de Mensagens
Este bot foi desenvolvido utilizando a biblioteca discord.py e permite agendar mensagens para serem enviadas em um canal do Discord em uma data e hora específica. O bot também suporta a menção a todos os usuários (@everyone), ao próprio usuário que fez o agendamento, ou a um cargo específico do servidor.

Funcionalidades
Agendamento de Mensagens: Permite que os usuários agendem mensagens para serem enviadas em um horário futuro.
Menções Personalizadas: As mensagens podem incluir menções a @everyone, ao próprio usuário que fez o agendamento ou a um cargo específico.
Exemplo de Uso
Para agendar uma mensagem, utilize o comando:

less
Copy code
!agendar DD-MM-AAAA-HH:MM [me/everyone/cargo] Sua mensagem aqui
Exemplos:

Agendar uma mensagem para todos:

diff
Copy code
!agendar 02-08-2024-15:30 everyone Lembrete importante!
Agendar uma mensagem para si mesmo:

diff
Copy code
!agendar 02-08-2024-15:30 me Não se esqueça da reunião!

Agendar uma mensagem mencionando um cargo específico:

diff
Copy code
!agendar 02-08-2024-15:30 Milionários Vamos nos encontrar às 16h!
Requisitos
Python 3.8 ou superior
Bibliotecas Python:
discord.py (pip install discord.py)

Funcionamento
Quando o bot estiver online, você poderá utilizar o comando !agendar no Discord para agendar uma mensagem.
O bot responderá confirmando o agendamento e enviará a mensagem no canal especificado no horário agendado.
As mensagens podem ser agendadas para incluir menções a @everyone, a si mesmo (me), ou a um cargo específico do servidor.


Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
