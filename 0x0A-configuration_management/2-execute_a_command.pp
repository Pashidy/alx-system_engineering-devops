# To execute the killmenow command
exec { 'pkill_killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
}
