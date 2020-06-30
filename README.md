<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/mac-speech-commands.svg?maxAge=3600)](https://pypi.org/project/mac-speech-commands/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-speech-commands.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-speech-commands.py/actions)

### Installation
```bash
$ [sudo] pip install mac-speech-commands
```

#### Examples
russian minutes plural:
```python
import mac_speech_commands
import plural_ru

def ru_minutes(value):
    return "%s %s" % (value.replace("1","одну"),plural_ru.ru(int(value),['минуту','минуты','минут']))

text="... длится [[ru:minutes 10]]"
functions = {"ru:minutes":ru_minutes}

mac_speech_commands.replace(text,functions)
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>