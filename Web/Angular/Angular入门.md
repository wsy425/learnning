1. 一整套企业级方案，基本不需要其他插件
2. 安装了augury插件方便浏览器检查angular
3. angular框架项目结构
   ![QQ截图20210321160902.png](https://i.loli.net/2021/03/21/piPK8VaBb2ok9rD.png)
4. 框架内容写在component.ts里，东西应用于html
# 条件渲染
   ```HTML
   <div *ngIf="判断条件 else 其他显示的ID"></div>
   <ng-template #ID>不满足判断条件时显示的内容</ng-template>
   ```
# 列表渲染
   ```HTML
   <ul>
    <li *ngFor="let item of 列表名;let i = index">
        {{item}}
    </li>
   </ul>
   ```
# 时间绑定
   ```HTML
   <button (事件名)="事件绑定的函数"></button>
   ```
# 类与样式绑定
   ```HTML
   <p [class]="'active'">文本内容</p>
   <style>
    .active{color:orange}
   </style>
   ```
# 表单绑定
## 手动双向绑定
    ```HTML
    <input type="text" [value] = "ts中的属性" (事件) = "函数">
    ```
## 自动双向绑定
FormsModule
    ```HTML
    <input type="text" [(ngModel)]="ts中的属性">
    ```