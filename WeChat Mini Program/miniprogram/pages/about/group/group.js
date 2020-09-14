// miniprogram/pages/group/group.js
const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,
  },
  pageBack() {
    wx.navigateBack({
      delta: 1
    });
  }
});