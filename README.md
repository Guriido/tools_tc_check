# tools_tc_check
Checks output of timecard 
creates a tool to check timecard from clipboard

## Requirements 

- python3

## Installation

```
$ git clone https://github.com/Guriido/tools_tc_check.git

$ cd tools_tc_check
$ python3 src/tc_setup.py

```

This will create a bash script `tc_check.sh` in `tools_tc_check` folder.

## Use

```
$ ./tc_check.sh """ %paste the tc output here% """
```

## Format

The inupt is a text expected to be of the following format (colonns positions can be interverted, and x are digits)

```
date(day) | in  | out |break-start|break-end|total |over_midnight|sick-leave|  holiday  
11/01(Thu)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/02(Fri)|     |     |           |         |      |             |   yes    |            
11/03(Sat)|     |     |           |         |      |             |          |  文化の日  
11/04(Sun)|     |     |           |         |      |             |          |            
11/05(Mon)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/06(Tue)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/07(Wed)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/08(Thu)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/09(Fri)|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|          |            
11/10(Sat)|     |     |           |         |      |             |          |            
11/11(Sun)|     |     |           |         |      |             |          |            
11/12(Mon)|xx:xx|xx:xx|           |         |xx:xx|xx:xx|          |            
11/13(Tue)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/14(Wed)|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|             |          |            
11/15(Thu)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/16(Fri)|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|             |          |            
11/17(Sat)|     |     |           |         |      |             |          |            
11/18(Sun)|     |     |           |         |      |             |          |            
11/19(Mon)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/20(Tue)|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|             |          |            
11/21(Wed)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/22(Thu)|xx:xx|xx:xx|           |         |xx:xx|xx:xx|          |            
11/23(Fri)|     |     |           |         |      |             |          |勤労感謝の日
11/24(Sat)|     |     |           |         |      |             |          |            
11/25(Sun)|     |     |           |         |      |             |          |            
11/26(Mon)|xx:xx|xx:xx|           |         |xx:xx|xx:xx|          |            
11/27(Tue)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/28(Wed)|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|             |          |            
11/29(Thu)|xx:xx|xx:xx|           |         |xx:xx|             |          |            
11/30(Fri)|xx:xx|xx:xx|xx:xx|xx:xx|xx:xx|             |          |            
         |     |     |           |         |xx:xx|xx:xx|          |     
```
