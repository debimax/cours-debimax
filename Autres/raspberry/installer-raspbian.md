# Comment  installer  raspbian




## installation raspbian

Télécharger la dernière image,  pour moi [Raspbian Stretch Lite](https://downloads.raspberrypi.org/raspbian_lite_latest).

```bash
# On télécharge
wget  https://downloads.raspberrypi.org/raspbian_lite_latest
# On  dézipe
unzip  2018-11-13-raspbian-strech-lite.zip
```


__Il est très important de savoir où est exactement votre carte sd__.  
Branchez votre carte sd (avec adaptateur) sur l'ordinateur:  
```bash
 sudo fdisk -l
```

Pour moi ca sera /dev/sd**b**  vous adaptez chez vous mais __attention__ à ne pas vous tromper.  
Je vous conseille de vérifier à chaque fois où est est votre carte sd au rique par exemple de formater votre propre système.  
```

On installe maintenant  rasbian

```bash
dd bs=1M if=2018-11-13-raspbian-stretch-lite.img of=/dev/sdb   status=progress conv=fsync
```

Remettre la carte sd sur le raspberry et booter.  Comme j'ai pris la version lite il faut se logguer.  

- login:  pi
- raspberry  (attention comme le clavier est qwerty  il faut taper rqspberry)

On va franciser la la clé

```bash
sudo  raspi-config   (rqspi-config)
```

*Remarque: Pour naviguer dans se menu il faut utiliser les flèches directionnel pour monter/descendre et la touche tabulation pour changer d'options, barre espace pour cocher/décocher les cases.*

_Choisir 4 Localisation Options et modifier:  
- I1 Change locale  (décocher en_GB.UTF-8 UTF-8   et choisir fr_FR.UTF-8 UTF-8
- I2 Change Timezone   (choisir Paris)
- I3 Change keybord Layout  (clavier  azery)

Vérifier que le clavier est bien azerty.

Arréter le raspberry avec  `sudo halt`

## changer pour une partition f2fs

[Ref: ](https://korben.info/f2fs-systeme-de-fichiers-pense-raspberry-pi-linstaller.html)



```bash
mkdir ~/backup_sd
mkdir  ~/tmp
# On monte la partion 2 de la carte sur le dossier ~/tmp
sudo mount /dev/sdb2  ~/tmp
# on sauvegarde le contenu de sb2. 
sudo cp -v -a ~/tmp/* ~/backup_sd
sudo umount ~/tmp
```


Une fois la copie terminée, on va installer le package f2fs-tools qui va nous permettre de formater en F2FS.  
```
sudo apt-get install f2fs-tools
```

On formate la partition:  
```
    sudo mkfs.f2fs /dev/sdb2
```

Débrancher la carte,  la rebrancher et __vérifier qu'on est toujours  en sdb2 avec ` sudo fdisk -l`__)

On remonte la partition:   
```
    sudo mount -t f2fs /dev/sdb2 ~/tmp
```

Et on copie dans l'autre sens  sur la carte sd:
```
    sudo cp -v -a ~/backup_sd/* ~/tmp/
```

On doit modifier  le fichier /etc/fstab de la carte mémoire.  
```
sudo editor ~/tmp/etc/fstab
```

Et modifiez la ligne concernant mmcblk0p2 (partition de votre carte sd) pour remplacer _ext4_ par ___f2fs___ et mettre les paramètres ___defaults,noatime,discard___  
```
    /dev/mmcblk0p2       /       f2fs        defaults,noatime,discard  0 1
```

On  démonte  
```bash
sudo umount  ~/tmp
```

On a un deuxième fichier à modifier sur la partition /sdb1  
```
  sudo mount /dev/sdb1 ~/tmp
  sudo editor ~/tmp/boot/cmdline.txt
```

et remplacez ext4 par f2fs dans le paramètre suivant ___`rootfstype=f2fs`___.  
```
sudo umount  ~/tmp
```

et enfin  rebooter le raspberry avec la carte sd.
