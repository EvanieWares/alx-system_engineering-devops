# Install flask from pip3.

# Update system
exec { 'apt update':
  command => '/usr/bin/apt-get update'
}

# Install flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Exec['apt update']
}
