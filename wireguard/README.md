# Ansible Wireguard Roles

Dans ce projet, on retrouve 3 rôles qui permettent d'installer Wireguard sur un serveur OpenBSD et de le configurer :

- Le rôle wg_installation se chargera de l'installation.
- Le rôle wg_setup_server va initialiser les clés et le fichier de configuration de Wireguard sur le serveur.
- Le rôle wg_add_user va :
  - Vérifier si les clés du serveur sont bien créées.
  - Créer les clés des clients.
  - Ajouter les nouveaux clients dans la configuration du serveur.

## Requirements

Le serveur cible doit être un OpenBSD. (testé sur BSD7.5)
Python 3 doit être installé sur celui-ci.
Le package wireguard-tools doit être installé manuellement. (pkg_add wireguard_tools)
La/Les configurations des instances wireguards serveur doivent être créée manuellement (création de la paire de clé)

```bash
$ umask 077
$ wg genkey > instance_name.key
$ wg pubkey < instance_name.key > instance_name.pub
```

wg0.conf example configuration: 

```bash
$ cat /etc/wireguard/instance_name/wg0.conf
[Interface]
PrivateKey=maximumsecurityprivatekey=
ListenPort=51820
Address = 192.168.0.1/24
```

Les ouvertures firewalls nécéssaire sont également à mettre en place.


## Execution
```
ansible-playbook -i inventory.yml playbook.yml
```

## Ajout de nouveaux utilisateurs

Rajouter les nom des utilisateurs à la liste "USER" définie par instances.

```yml
USERS:
  - MITNICK_Kevin

```

## Suppression user

Pour supprimer un utilisateur il suffit de le supprimmer de la liste presente dans la variable `WIREGUARD_USERS`.
