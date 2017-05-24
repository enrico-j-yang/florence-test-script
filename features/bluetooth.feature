# -*- coding: utf-8 -*-
# language: zh-CN

功能: 蓝牙
============================================
    蓝牙连接、蓝牙音乐、蓝牙电话
    
    @BluetoothConnection
    场景:   蓝牙初次配对连接
        假如    面板蓝牙未配对
        当      用户使用蓝牙设备连接电动车面板蓝牙
        那么    面板进入系统设置

        当      用户输入PIN码0000
        那么    面板显示蓝牙已连接

        当      用户长按O键
        那么    面板进入系统设置

        当      用户长按O键
        那么    面板进入主界面
        而且    面板显示蓝牙图标
    
    @BluetoothConnection
    场景:   蓝牙初次配对PIN码错误，配对失败
        假如    面板蓝牙未配对
        当      用户使用蓝牙设备连接电动车面板蓝牙
        那么    面板进入系统设置
        
        当      用户输入PIN码9999
        那么    面板显示蓝牙未连接

        当      用户长按O键
        那么    面板进入系统设置

        当      用户长按O键
        那么    面板进入主界面
        而且    面板不显示蓝牙图标
    
    @BluetoothConnection
    场景:   蓝牙初次配对不输入配对码，配对失败
        假如    面板蓝牙未配对
        当      用户使用蓝牙设备连接电动车面板蓝牙
        那么    面板进入系统设置
        
        当      用户不输入配对码
        那么    面板显示蓝牙未连接

        当      用户长按O键
        那么    面板进入系统设置

        当      用户长按O键
        那么    面板进入主界面
        而且    面板不显示蓝牙图标
    
    @BluetoothConnection
    场景:   蓝牙已有配对设备面板自动连接已配对的蓝牙设备
        假如    面板蓝牙已有配对设备
        当      用户启动电动车
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接

        假如    面板蓝牙可以连接蓝牙设备
        当      用户等待7秒后
        那么    面板显示蓝牙正在连接

        当      用户等待5秒后
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        那么    面板显示蓝牙图标
    
    @BluetoothConnection
    场景:   蓝牙已有配对设备面板自动连接已配对的蓝牙设备失败，15秒后重连成功
        假如    面板蓝牙已有配对设备
        当      用户启动电动车
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接

        假如    面板蓝牙不可以连接蓝牙设备
        当      用户等待7秒后
        那么    面板显示蓝牙正在连接

        当      用户等待5秒后
        那么    面板显示蓝牙未连接
        
        当      用户等待15秒后
        那么    面板显示蓝牙正在连接
        
        假如    面板蓝牙可以连接蓝牙设备
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        那么    面板显示蓝牙图标
    
    @BluetoothConnection
    场景:   蓝牙已有配对设备面板自动连接已配对的蓝牙设备失败，15秒后重连也失败
        假如    面板蓝牙已有配对设备
        当      用户启动电动车
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接

        假如    面板蓝牙不可以连接蓝牙设备
        当      用户等待7秒后
        那么    面板显示蓝牙正在连接

        当      用户等待5秒后
        那么    面板显示蓝牙未连接

        假如    面板蓝牙不可以连接蓝牙设备
        当      用户等待15秒后
        那么    面板显示蓝牙正在连接

        当      用户等待5秒后
        那么    面板显示蓝牙未连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        那么    面板不显示蓝牙图标
    
    @BluetoothConnection
    场景:   蓝牙已有配对设备，重新配对
        假如    面板蓝牙已有配对设备
        当      用户启动电动车
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接
        
        当      用户等待7秒后
        那么    面板显示蓝牙正在连接
        
        当      用户短按+键
        那么    面板显示蓝牙未连接
        
        当      用户使用蓝牙设备连接电动车面板蓝牙
        那么    面板显示蓝牙正在连接
        
        假如    面板蓝牙可以连接蓝牙设备
        当      用户输入PIN码0000
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        那么    面板显示蓝牙图标
    
    @BluetoothMusic
    场景:   蓝牙音乐信息显示
        假如    面板已经连接手机蓝牙
        当      用户在手机上播放音乐
        那么    面板显示音乐歌曲名和歌手名
    
    @BluetoothMusic
    场景:   蓝牙音乐播放与暂停
        假如    面板已经连接手机蓝牙
        当      用户在手机上播放音乐
        那么    面板显示音乐歌曲名和歌手名
        
        当      用户在手机上暂停音乐
        那么    面板不显示音乐歌曲名和歌手名

        当      用户在手机上播放音乐
        那么    面板显示音乐歌曲名和歌手名
    
    @BluetoothMusic
    场景:   蓝牙音乐音量调节
        假如    面板已经连接手机蓝牙
        当      用户在手机上播放音乐
        那么    面板显示音乐歌曲名和歌手名
        
        当      用户短按10次-键
        那么    面板显示音量减少到静音
        
        当      用户短按10次+键
        那么    面板显示音量增加到最大
    
    @BluetoothMusic
    场景:   蓝牙音乐上一首下一首
        假如    面板已经连接手机蓝牙
        当      用户在手机上播放音乐
        那么    面板显示音乐歌曲名和歌手名
        
        当      用户长按-键
        那么    面板显示上一首歌曲名和歌手名
        而且    面板蓝牙播放上一首歌曲
        
        当      用户长按+键
        那么    面板显示下一首歌曲歌曲名和歌手名
        而且    面板蓝牙播放下一首歌曲
    
    @BluetoothCall
    场景:   蓝牙电话来电
        假如    面板已经连接手机蓝牙
        当      用户使用另一台手机拨打已连接面板蓝牙的手机
        那么    面板显示来电图标和来电号码
        
        当      用户接听电话
        那么    面板显示通话图标和通话号码
        
        当      用户挂断电话
        那么    面板显示挂断图标和挂断号码
    
    @BluetoothCall
    场景:   蓝牙电话拨打
        假如    面板已经连接手机蓝牙
        当      用户使用已连接面板蓝牙的手机拨打另一台手机
        那么    面板显示拨打图标和拨打号码
        
        当      用户接听电话
        那么    面板显示通话图标和通话号码
        
        当      用户挂断电话
        那么    面板显示挂断图标和挂断号码
    
    @BluetoothCall
    场景:   蓝牙音乐播放中电话来电
        假如    面板已经连接手机蓝牙
        假如    面板蓝牙音乐播放中
        当      用户使用另一台手机拨打已连接面板蓝牙的手机
        那么    面板暂停音乐播放
        那么    面板显示来电图标和来电号码
        
        当      用户接听电话
        那么    面板显示通话图标和通话号码
        
        当      用户挂断电话
        那么    面板显示挂断图标和挂断号码
        那么    面板恢复音乐播放
        而且    面板返回音乐播放界面
    
    @BluetoothCall
    场景:   蓝牙音乐播放中电话拨打
        假如    面板已经连接手机蓝牙
        假如    面板蓝牙音乐播放中
        当      用户使用已连接面板蓝牙的手机拨打另一台手机
        那么    面板暂停音乐播放
        那么    面板显示拨打图标和拨打号码
        
        当      用户接听电话
        那么    面板显示通话图标和通话号码
        
        当      用户挂断电话
        那么    面板显示挂断图标和挂断号码
        那么    面板恢复音乐播放
        而且    面板返回音乐播放界面
        
        
        
        
        
    
    
        
    