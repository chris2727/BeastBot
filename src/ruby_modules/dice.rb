#!/usr/bin/env ruby

# This script throws the dice
#
# Author: Lenoch

require 'beastbot'

def throw(sides)
  value = Random.rand(sides)
  return value.to_s
end

sides = Beastbot::Interpret::get_arguments
val = throw(sides.to_i)
Beastbot::Talk::send_to_channel("Throws " + val)
