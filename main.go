package main

import (
	"fmt"
	"os"

	"github.com/urfave/cli/v2"
)

func main() {
	app := &cli.App{
		Name:  "ssh-key-manager",
		Usage: "Manage SSH keys",
		Commands: []*cli.Command{
			{
				Name:   "add-key",
				Usage:  "Add a new SSH key",
				Action: addSSHKey,
				Flags: []cli.Flag{
					&cli.StringFlag{
						Name:     "username",
						Aliases:  []string{"u"},
						Required: true,
						Usage:    "Username",
					},
					&cli.StringFlag{
						Name:     "name",
						Aliases:  []string{"n"},
						Required: true,
						Usage:    "Key name",
					},
					&cli.StringFlag{
						Name:     "public-key",
						Aliases:  []string{"k"},
						Required: true,
						Usage:    "Public key",
					},
				},
			},
			// Add more commands (e.g., list-keys, delete-key) as needed
		},
	}

	if err := app.Run(os.Args); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
func addSSHKey(c *cli.Context) error {
	// Implement the logic to add an SSH key here
	username := c.String("username")
	keyName := c.String("name")
	publicKey := c.String("public-key")

	// Example: Print the publicKey
	fmt.Printf("Added SSH key '%s' for user '%s' with publicKey: %s\n", keyName, username, publicKey)

	// Your actual logic to add the SSH key to the user's profile

	return nil
}
