# To ensure the operating system functions using the 'Holberton' entry key without error

exec { 'ensure-holberton-hard-limit':
  command => 'echo "holberton hard nofile 50000" >> /etc/security/limits.conf',
  unless  => 'grep -q "holberton hard nofile" /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin',
}

exec { 'ensure-holberton-soft-limit':
  command => 'echo "holberton soft nofile 50000" >> /etc/security/limits.conf',
  unless  => 'grep -q "holberton soft nofile" /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin',
}

exec { 'increase-hard-file-limit-holberton-user':
  command => 'sed -i "/holberton hard nofile/s/[0-9]\+/50000/" /etc/security/limits.conf',
  onlyif  => 'grep -q "holberton hard nofile" /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin',
  require => Exec['ensure-holberton-hard-limit'],
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft nofile/s/[0-9]\+/50000/" /etc/security/limits.conf',
  onlyif  => 'grep -q "holberton soft nofile" /etc/security/limits.conf',
  path    => '/usr/local/bin:/usr/bin:/bin',
  require => Exec['ensure-holberton-soft-limit'],
}
