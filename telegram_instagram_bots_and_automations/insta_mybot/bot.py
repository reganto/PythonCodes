#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from instabot_py import InstaBot

bot = InstaBot(
    login='',
    password='argon2-cffi',
        
    like_per_day = 250,
    comments_per_day = 0,
    max_like_for_one_tag = 36,
    follow_per_day = 0,
    follow_time = 36000,
    unfollow_per_day = 0,
    unfollow_break_min = 3,
    unfollow_break_max = 17,
    log_mod = 0,
    proxy = '',
    unfollow_selebgram = False,
    unfollow_probably_fake = True,
    unfollow_inactive = True,
    unfollow_recent_feed = False,
    tag_blacklist = ["rain", "thunderstorm"],
    unwanted_username_list = ["second", "stuff", "art", "project", "love", "life", "food", "blog", "free", "keren", "photo", "graphy", "indo", "travel", "art", "shop", "store", "sex", "toko", "jual", "online", "murah", "jam", "kaos", "case", "baju", "fashion", "corp", "tas", "butik", "grosir", "karpet", "sosis", "salon", "skin", "care", "cloth", "tech", "rental", "kamera", "beauty", "express", "kredit", "collection", "impor", "preloved", "follow", "follower", "gain", ".id", "_id", "bags"],
    unfollow_whitelist=['jadijadinet'],

    tag_list=[
        'ایران',
        'ایرانی',
        'ایرانگردی',
        'خوشمزه',
        'رفیق',
        'تهران',
        'تهرانگردی',
        'خاطره',
        'عشق',
        'عکس',
        'عکاسی',
        'تهراني',
        'خاطره',
        'قديمي',
        'بازيگر',
        'خواننده',
        'پول',
        'انگیزه',
        'انگیزشی',
        'جذب',
        'روانشناس',
        'ایرانیان',
        'کتاب',
        'ویدیو',
        'خنده',
        'خنده_دار',
        'غم',
        'من',
        'تو',
        'مادر',
        'پدر',
        'خواب',
        'شمال',
        'اصفهان',
        'تبریز',
        'خوزستان',
        'مشهد',
        'خراسان',
        'موفقیت',
        'زن',
        'مرد',
        'مردانه',
        'دختر',
        'دخترانه',
        'دخترونه',
        'پسر',
        'استقبال',
        'استقلال',
        'پرسپولیس',
        'ثروت',
        'محبت',
        'آزدی',
        'زندگی',
        'خوب',
        'آزاد',
        'زیبا',
        'زیبایی',
        'غمگین',
        'زندگی',
        'پارس',
        'خلیج_فارس',
        'فالو',
        'فالوور',
        'لایک',
        'کامنت',
        'تاریخ',
        'تاریخی',
        'iran',
        'irani',
        'iran_aks_mobile',
        'iranemoon',
        'iraninsta',
        'iranian_photography',
        'iran_traveling',
        'isfahan',
        'radiojavan',
        'tehrani',
        'جوان',
        'جوانی',
        'جوانان',
        'طبیعت',
        'طبیعتگردی',
        'طبیعت_گردی',
        'کوه',
        'کوهنوردی',
        'کوهستان',
        'negasonic',
        'teenage'
        'motogp'
        'python',
        'linux'
    ],
)

bot.mainloop()
