# DroneKit Kullanımı

This is an example markdown format text for DroneKit Tutorial.
## Sub Title
* Here is an code import example

This is bash code example
```bash
  sudo apt update
```
Here is another example
```bash
  sudo apt update
```
This is a python code example
```python
  print("Hello World")
```
Here is another example `variable`


# Sanal Makinaya Ubuntu Kurmak

DroneKit kütüphanesi kullanmak için önecelikle Ubuntu işletim sistemine sahip bir bilgisayara ihtiyaç duyuyoruz. Windows işletim sisteminde sanal bilgisayar yazılımları ile bu ihtiyacımızı karşılıyabiliyoruz

VMware programının setup dosyasını indirmek için : https://www.vmware.com/products/workstation-player/workstation-player-evaluation.html

Ubuntu işletim sisteminin İSO dosyasını indirmek için : https://releases.ubuntu.com/18.04.6/?_ga=2.59504109.1117219064.1700847152-2047495795.1700847152

Detaylı anlatım videosu : 

# Gerekli Programların Kurulması

DroneKit ile drone programlama için gerekli olan programlar

* Ardupilot SITL

* Gazebo

* DroneKit

## Ardupilot SITL

Ardupilot SITL programını kurmak için öncelikle Git'i kurmamız gerekiyor

```bash
  sudo apt-get update
  sudo apt-get upgrade
```


```bash
  sudo apt-get install git
  sudo apt-get install gitk git-gui
```

Git üzerinden Ardupilot SITL dosyalarını indirme

```bash
  git clone https://github.com/ArduPilot/ardupilot.git
```

Gerekli Bileşenlerin Yüklenmesi

```bash
  sudo apt install python-matplotlib python-serial python-wxgtk4.0 python-wxtools
  python-lxml python-scipy python-opencv ccache gawk python-pip python-pexpect

```
