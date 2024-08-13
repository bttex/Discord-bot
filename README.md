# Discord Bot para Agendamento de Mensagens

Este bot foi desenvolvido utilizando a biblioteca discord.py e permite agendar mensagens para serem enviadas em um canal do Discord em uma data e hora específica. O bot também suporta a menção a todos os usuários (@everyone), ao próprio usuário que fez o agendamento, ou a um cargo específico do servidor.

## Funcionalidades

Agendamento de Mensagens: Permite que os usuários agendem mensagens para serem enviadas em um horário futuro.

Menções Personalizadas: As mensagens podem incluir menções a @everyone, ao próprio usuário que fez o agendamento ou a um cargo específico.

## Instalação

### Requisitos

Python 3.8 ou superior

Bibliotecas Python:



```bash
discord.py (pip install discord.py)
```

## Exemplo de Uso
Para agendar uma mensagem, utilize o comando:

```python
!agendar DD-MM-AAAA-HH:MM [me/everyone/cargo] Sua mensagem aqui
```

### Exemplos

Agendar uma mensagem para todos:

```python
!agendar 02-08-2024-15:30 everyone Lembrete importante!
```
Agendar uma mensagem para si mesmo:

```python
!agendar 02-08-2024-15:30 everyone Lembrete importante!
```

Agendar uma mensagem mencionando um cargo específico:

```python
!agendar 02-08-2024-15:30 [Cargo] Vamos nos encontrar às 16h!
```


## License

[MIT](https://choosealicense.com/licenses/mit/)
