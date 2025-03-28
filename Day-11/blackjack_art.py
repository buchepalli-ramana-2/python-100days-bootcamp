cards = r'''
.------..------.   
|A.--. ||K.--. |
| (\/) || :/\: |
| :\/: || :\/: |
| '--'A|| '--'K|
`------'`------'
'''
title = r''' 
_______   ___            __       ______   __   ___       ___      __       ______   __   ___  
|   _  "\ |"  |          /""\     /" _  "\ |/"| /  ")     |"  |    /""\     /" _  "\ |/"| /  ") 
(. |_)  :)||  |         /    \   (: ( \___)(: |/   /      ||  |   /    \   (: ( \___)(: |/   /  
|:     \/ |:  |        /' /\  \   \/ \     |    __/       |:  |  /' /\  \   \/ \     |    __/   
(|  _  \\  \  |___    //  __'  \  //  \ _  (// _  \    ___|  /  //  __'  \  //  \ _  (// _  \   
|: |_)  :)( \_|:  \  /   /  \\  \(:   _) \ |: | \  \  /  :|_/ )/   /  \\  \(:   _) \ |: | \  \  
(_______/  \_______)(___/    \___)\_______)(__|  \__)(_______/(___/    \___)\_______)(__|  \__) 
                                                                                          
'''

spacer = " "*5
for a,b in zip(cards.splitlines(),title.splitlines()):
    print(f"{a}{spacer}{b}")