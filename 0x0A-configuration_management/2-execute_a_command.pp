#!/usr/bin/pup
# To execute the killmenow command

exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}

