import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')

  user_option = input('piedra, papel o tijera => ')
  user_option = user_option.lower()

  if user_option not in options:
    print(user_option + ' no es una opción válida')
    #continue
    return None, None

  computer_option = random.choice(options)

  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano')
      computer_wins += 1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano')
      computer_wins += 1
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano')
      computer_wins += 1
  return user_wins, computer_wins


def check_winner(user_wins, computer_wins, rounds):
  if computer_wins == 2:
    print('El ganador es la computadora')
    print('ROUND', rounds, '=>', 'user: ', user_wins, '- computer: ',
          computer_wins)
    print('Juego terminado')
    exit()

  if user_wins == 2:
    print('El ganador es el usuario')
    print('ROUND', rounds, '=>', 'user: ', user_wins, '- computer: ',
          computer_wins)
    print('Juego terminado')
    exit()


def run_game():
  computer_wins = 0
  user_wins = 0
  rounds = 1
  while True:
    print('*' * 10)
    print('ROUND', rounds, '=>', 'user: ', user_wins, '- computer: ',
          computer_wins)
    print('*' * 10)

    rounds += 1

    user_option, computer_option = choose_options()

    user_wins, computer_wins = check_rules(user_option, computer_option,
                                           user_wins, computer_wins)

    check_winner(user_wins, computer_wins, rounds)


run_game()
