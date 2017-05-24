# -*- coding: utf-8 -*-
# language: zh-CN

功能: 设置
============================================
    蓝牙设置、时间设置、亮度设置、语言设置
    
    @BluetoothSetting
    场景:   面板设置蓝牙，未连接
        假如    面板蓝牙未连接
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        而且    面板不显示蓝牙图标
    
    @BluetoothSetting
    场景:   面板设置蓝牙，正在连接
        假如    面板蓝牙未连接
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙未连接
        
        当      用户使用蓝牙设备连接电动车面板蓝牙
        那么    面板显示蓝牙正在连接

        当      用户的蓝牙设备已经连接上电动车面板蓝牙
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        而且    面板显示蓝牙图标
        
    @BluetoothSetting
    场景:   面板设置蓝牙，已连接
        假如    面板蓝牙已连接
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户长按O键
        那么    面板进入主界面
        而且    面板显示蓝牙图标
        
    @BluetoothSetting
    场景:   面板设置蓝牙，重新配对
        假如    面板蓝牙已连接
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按O键
        那么    面板显示蓝牙已连接
        
        当      用户短按+键
        那么    面板显示蓝牙从已连接变为未连接
        
        当      用户使用蓝牙设备连接电动车面板蓝牙
        那么    面板显示蓝牙正在连接
        
        当      用户的蓝牙设备已经连接上电动车面板蓝牙
        那么    面板显示蓝牙已连接
        
        当      用户长按O键
        那么    面板进入主界面
        而且    面板显示蓝牙图标
    
    @Time
    场景:   面板设置时间
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按+键
        那么    面板显示为时间
        
        当      用户短按O键
        那么    面板显示时间设置的时间，并选中时钟
        
        当      用户短按+键
        那么    面板小时数增加
        
        当      用户短按-键
        那么    面板小时数减少
        
        当      用户长按+键
        那么    面板小时数持续增加
        
        当      用户长按-键
        那么    面板小时数持续减少
        
        当      用户短按O键
        那么    面板确认小时调节，并选中分钟
        
        当      用户短按+键
        那么    面板分钟数增加
        
        当      用户短按-键
        那么    面板分钟数减少
        
        当      用户长按+键
        那么    面板分钟数持续增加
        
        当      用户长按-键
        那么    面板分钟数持续减少
        
        当      用户短按O键
        那么    面板确认调节并返回时间菜单
        
        当      用户长按O键
        那么    面板进入主界面
    
    @Time
    场景:   面板取消设置时间
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按+键
        那么    面板显示为时间
        
        当      用户短按O键
        那么    面板显示时间设置的时间，并选中时钟
        
        当      用户短按+键
        那么    面板小时数减少
        
        当      用户短按O键
        那么    面板确认小时调节，并选中分钟
        
        当      用户短按-键
        那么    面板分钟数增加
        
        当      用户长按O键
        那么    面板取消调节并返回时间菜单
        
        当      用户长按O键
        那么    面板返回主界面，时间不变
    
    @Brightness
    场景:   面板设置亮度
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按2次+键
        那么    面板显示为亮度
        
        当      用户短按O键
        那么    面板显示初始亮度为6格
        
        当      用户短按4次+键
        那么    面板亮度增加到最大
        
        当      用户短按9次-键
        那么    面板亮度减少到最小
        
        当      用户短按O键
        那么    面板确认调整并返回亮度菜单
        
        当      用户长按O键
        那么    面板进入主界面
    
    @Brightness
    场景:   面板取消设置亮度
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按2次+键
        那么    面板显示为亮度
        
        当      用户短按O键
        那么    面板显示初始亮度为6格
        
        当      用户短按4次+键
        那么    面板亮度增加到最大
        
        当      用户短按9次-键
        那么    面板亮度减少到最小
        
        当      用户长按O键
        那么    面板取消调节并返回亮度菜单
        
        当      用户长按O键
        那么    面板进入主界面
    
    @Language
    场景:   面板设置语言为繁体
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按3次+键
        那么    面板显示为语言
        
        当      用户短按O键
        那么    面板显示高亮为繁体
        
        当      用户短按O键
        那么    面板切换系统语言为繁体并返回语言菜单
        
        当      用户长按O键
        那么    面板进入主界面
    
    @Language
    场景:   面板设置语言为简体
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按3次+键
        那么    面板显示为语言
        
        当      用户短按O键
        那么    面板显示三种语言选择
        
        当      用户短按1次+键
        那么    面板显示高亮为简体
        
        当      用户短按O键
        那么    面板切换系统语言为简体并返回语言菜单
        
        当      用户长按O键
        那么    面板进入主界面
    
    @Language
    场景:   面板设置语言为简体
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按3次+键
        那么    面板显示为语言
        
        当      用户短按O键
        那么    面板显示三种语言选择
        
        当      用户短按2次+键
        那么    面板显示高亮为English
        
        当      用户短按O键
        那么    面板切换系统语言为English并返回语言菜单
        
        当      用户长按O键
        那么    面板进入主界面
    
    @Language
    场景:   面板取消设置语言
        当      用户长按O键
        那么    面板进入系统设置
        
        当      用户短按3次+键
        那么    面板显示为语言
        
        当      用户短按O键
        那么    面板显示三种语言选择
        
        当      用户短按2次+键
        那么    面板显示高亮为English
        
        当      用户长按O键
        那么    面板返回语言菜单并且系统语言不变
        
        当      用户长按O键
        那么    面板进入主界面
        
        
        
    
    
        
    