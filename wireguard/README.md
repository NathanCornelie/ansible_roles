# Ansible Wireguard Roles

Dans ce projet, on retrouve 3 rôles qui permettent d'installer Wireguard sur un serveur OpenBSD et de le configurer :

- Le rôle wg_installation se chargera de l'installation.
- Le rôle wg_setup_server va initialiser les clés et le fichier de configuration de Wireguard sur le serveur.
- Le rôle wg_add_user va :
  - Vérifier si les clés du serveur sont bien créées.
  - Créer les clés des clients.
  - Ajouter les nouveaux clients dans la configuration du serveur.

## Identification

Les identifiants et les mots de passe des machines sont dans des fichiers chiffrés vault.yml dans les répertoires `group_vars/clients/` ou `group_vars/servers/` , dont la clé de déchiffrement est demandée au lancement du playbook.

## Ajout de nouveaux utilisateurs

Pour ajouter un nouvel utilisateur à la configuration du VPN, il suffit de l'ajouter au fichier `group_vars/servers/vars.yml` dans la variable `WIREGUARD_USERS`, ainsi que les IP avec lesquelles cet utilisateur va se connecter.

```yml
WIREGUARD_USERS:
  - name: CornelieNathan
    ips:
      - 10.0.0.2
      - 10.0.0.4

  - name: MarieLaS 
    ips:
      - 10.0.0.3
      - 10.0.0.5
```

## Suppression user

Pour supprimer un utilisateur il suffit de le supprimmer de la liste presente dans la variable `WIREGUARD_USERS`.

La commande pour exécuter ce playbook est la suivante:

```bash
ansible-playbook -i inventory.yml playbook.yml --ask-vault-password
```
