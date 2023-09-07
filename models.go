package main

type SSHKey struct {
	Name      string
	PublicKey string
}

type UserProfile struct {
	Username string
	SSHKeys  []SSHKey
}
