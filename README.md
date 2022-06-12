# AudioBook

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

### Use your PDF as a audiobook 🎧.

## Use on your system

Clone this repository on your system and run the following command

> **Note**
> Make sure you have python installed on your system.

```bash
pip -r install requirements.txt
```
```bash
python app.py
```

## Configurations

### Use you PDF

to use your own PDF edit line on. 12

```python
file = 'YOUR_PDF_FILE_PATH'
```

### Change Voice

to change audiobook voice

```python
engine.setProperty('voice', voices[1].id) # female
```
```python
engine.setProperty('voice', voices[0].id) # male
```

### Change speaking rate
to change speaking rate

```python
engine.setProperty(rate, ANY_NUMBER_YOU_WANT)
```
