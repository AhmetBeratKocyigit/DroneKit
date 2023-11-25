# DroneKit Kullanımı


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

### Git Kurulumu

```bash
sudo apt-get update
```

```bash
sudo apt-get upgrade
```


```bash
sudo apt-get install git
```

```bash
sudo apt-get install gitk git-gui
```

### Git üzerinden Ardupilot SITL dosyalarını indirme

```bash
git clone https://github.com/ArduPilot/ardupilot.git
```

### Gerekli Bileşenlerin Yüklenmesi

```bash
cd ardupilot
```

```bash
git submodule update --init --recursive
```

```bash
sudo apt install python-matplotlib python-serial python-wxgtk4.0 python-wxtools
python-lxml python-scipy python-opencv ccache gawk python-pip python-pexpect

```

```bash
gedit ~/.bashrc
```
.bashrc dosyası açıldıktan sonra en alt satıra inerek alttaki iki satırı yapıştırmanız gerekiyor

```bash
export PATH=$PATH:$HOME/ardupilot/Tools/autotest
export PATH=/usr/lib/ccache:$PATH
```


```bash
. ~/.bashrc
```

```bash
sudo pip install future pymavlink MAVProxy
```

### Ve Son Olarak Programın Çalıştırılması

```bash
cd ~/ardupilot/ArduCopter
```

```bash
  ../Tools/autotest/sim_vehicle.py -w --console --map
```
