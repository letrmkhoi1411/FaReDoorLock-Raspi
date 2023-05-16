import matrixKeyboard
import lcd1602
from servo import RunMotor
import time

STATE_A = 0
STATE_B = 1
STATE_C = 2
STATE_D = 3

def loop():
    kp = matrixKeyboard.keypad()
    lcd = lcd1602.lcd()
    password = 1234
    input_pass = 0
    new_pass = 0
    cur_state = STATE_A
    lcd.clear()
    lcd.message('Enter Password')
    time.sleep(0.5)
    # Loop while waiting for a keypress
    while True:

        key_val = kp.getKey()

        if key_val is not None:

            if cur_state == STATE_A:
                if key_val == 'B':
                    cur_state = STATE_B
                    lcd.clear()
                    lcd.message('Set Password')
                    time.sleep(0.5)
                elif key_val == 'C':
                    cur_state = STATE_C
                    lcd.clear()
                    lcd.message('FaRe Mode')
                    time.sleep(0.5)
                elif key_val == 'D':
                    cur_state = STATE_D
                    lcd.clear()
                    lcd.message('Add Face')
                    time.sleep(0.5)
                elif key_val == '#':
                    if input_pass == password:
                        lcd.clear()
                        lcd.message('Door Open!')
                        time.sleep(0.5)
                        RunMotor()
                        lcd.clear()
                        lcd.message('Enter Password')
                        time.sleep(0.5)
                    else:
                        lcd.clear()
                        lcd.message('Wrong Password')
                        time.sleep(1.5)
                        lcd.clear()
                        lcd.message('Enter Again!')
                    input_pass = 0
                elif key_val == '*':
                    input_pass = input_pass / 10
                    lcd.clear()
                    lcd.message(str(input_pass))
                    time.sleep(0.5)
                elif key_val in [0,1,2,3,4,5,6,7,8,9]:
                    input_pass = input_pass * 10 + key_val
                    lcd.clear()
                    lcd.message(str(input_pass))
                    time.sleep(0.5)

            elif cur_state == STATE_B:
                if key_val == 'A':
                    cur_state = STATE_A
                    lcd.clear()
                    lcd.message('Enter Password')
                    time.sleep(0.5)
                elif key_val == 'C':
                    cur_state = STATE_C
                    lcd.clear()
                    lcd.message('FaRe Mode')
                    time.sleep(0.5)
                elif key_val == 'D':
                    cur_state = STATE_D
                    lcd.clear()
                    lcd.message('Add Face')
                    time.sleep(0.5)
                elif key_val == '#':
                    password = new_pass
                    lcd.clear()
                    lcd.message('Set!')
                    time.sleep(0.5)
                    lcd.clear()
                    lcd.message(str(password))
                    time.sleep(0.5)
                    new_pass = 0
                elif key_val == '*':
                    new_pass = new_pass / 10
                    lcd.clear()
                    lcd.message(str(new_pass))
                    time.sleep(0.5)
                elif key_val in [0,1,2,3,4,5,6,7,8,9]:
                    new_pass = new_pass * 10 + key_val
                    lcd.clear()
                    lcd.message(str(new_pass))
                    time.sleep(0.5)

            elif cur_state == STATE_C:
                if key_val == 'A':
                    cur_state = STATE_A
                    lcd.clear()
                    lcd.message('Enter Password')
                    time.sleep(0.5)
                elif key_val == 'B':
                    cur_state = STATE_B
                    lcd.clear()
                    lcd.message('Set Password')
                    time.sleep(0.5)
                elif key_val == 'D':
                    cur_state = STATE_D
                    lcd.clear()
                    lcd.message('Add Face')
                    time.sleep(0.5)

            elif cur_state == STATE_D:
                if key_val == 'A':
                    cur_state = STATE_A
                    lcd.clear()
                    lcd.message('Enter Password')
                    time.sleep(0.5)
                elif key_val == 'B':
                    cur_state = STATE_B
                    lcd.clear()
                    lcd.message('Set Password')
                    time.sleep(0.5)
                elif key_val == 'C':
                    cur_state = STATE_C
                    lcd.clear()
                    lcd.message('FaRe Mode')
                    time.sleep(0.5)


if __name__ == '__main__':
    loop()