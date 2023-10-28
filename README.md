<h1 id="-div-align-center-dnf-div-"><div align="center"> DNF 奶量计算器 </div></h1>
<h2 id="-">一.预览</h2>
<img width="850" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/V1.2.png">
<h2 id="-">二.使用及说明</h2>
<h3 id="-buff-">
<font color=#FF0000> 使用前需注意,如果站街穿的不是BUff换装上的装备要穿上,否则站街Buff会算不准!</font>
</h3>
<ol>
<li><strong>增益量:</strong> 照填即可<font color=#6495ED> (位置:按键(M)-&gt;详细信息-&gt;增益量)</font></li>
<li><strong>站街属性:</strong> 照填即可</li>
<li><strong>进图补正:</strong> 可以不填,此栏主要是为了推算出下方进图 Buff 适用四维,推算结果不一定准确,具体请以实际进图为准.<font color=#6495ED>(目前影响推算结果的有:附魔装备,无畏鞋子,活动Buff等等)</font></li>
<li><strong>Buff 适用/一绝适用:</strong> 填写实际多人组队进图的属性</li>
<li><strong>智力加减:</strong><font color=#FF7F50>输入(+,-)号加数字</font> ,正号可以忽略不写.此项会对<font color=#FF7F50>站街智力,buff 适用智力,太阳适用智力</font>,进行加减并计算结果</li>
<li><strong>辟邪玉&amp;宠物&amp;&amp;光环&amp;武器:</strong> 固定三攻填写<font color=#FF7F50>身上所有固定三攻总和</font>,百分比三攻<font color=#FF7F50>每项请用逗号(,)隔开</font><font color=#6495ED>(辟邪玉为单独的一项)</font>,固定力智与百分比力智同理,其余照填即可.</li>
<li><strong>针对辟邪玉:</strong>不要看辟邪玉的<font color=#FF7F50>内部词条</font><img width="100" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/辟邪玉1.png">,请按下图对应填写<img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/辟邪玉2.png"></li>
<li><strong>其他:</strong> 在点击 <strong>设为基础</strong><font color=#A9A9A9> 数据变灰</font>后，如果 <font color=#FF7F50>输入(+,-)号加数字</font>,那么软件会以变灰的数据为基础进行计算,理论三攻误差±1,力智误差±10.</li>
</ol>
<strong>可能会有的更新(备忘)</strong><br>
1.添加一个对于C的相对提百分比提升显示<br>
2.类似光环宠物等1~95技能等级加+1,对于此类加等级的装备如果手动计算非常麻烦.思路:增加一个弹出面板,计算出增加的四维,然后再加到计算器里去.需要考虑到技能的成长曲线包括(是否线性成长，是否有上限).<br>
3.Bug-0X1.输入0开头的数计算会直接退出.<br>
<h2 id="-">三.示例</h2>
<h3 id="-">下面以奶妈为例,进行简单计算</h3>
<h4 id="-">1.1面板(未穿项链)</h4>
<p>
<img width="400" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/5.png">
<img width="300" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/辟邪玉2.png">
  <h6 id="-">护士:8%,4%,4%</h6>
  <h6 id="-">宠物Buff量:5%</h6>
  <h6 id="-">光环Buff量:5%</h6>
</p>
<h4 id="-">1.2填写</h4>
<img width="400" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/9.png">
<h4 id="-">1.3结果&实际</h4>
<p>
  <img width="300" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/10.png" >
  <img width="300" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/11.png">
  <br>
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/6.png">
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/7.png">
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/4.png">
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/2.png">
<h6 id="-">误差为0</h6>
</p>
<h4 id="-">2.1穿上项链&填写</h4>
<p>
<img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/12.png">
<img width="300" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/a2.png">
</p>
<h6 id="-">智力:15+15+150+107+90=377</h6>
<h6 id="-">增益量:295(基础)+5575(成长)+1518(贴膜)=7388</h6>
<h6 id="-">进图Buff+1,一绝+1</h6>
<h4 id="-">2.2结果&实际</h4>
<p><img width="450" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/a1.png"><br>
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/14.png">
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/3.png">
  <img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/1.png">
</p>
<h4 id="-">3.1更换辟邪玉&填写</h4>
<P>
<img width="300" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/13.png">
<img width="300" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/b1.png">
</P>
<h4 id="-">3.2结果&实际</h4>
<img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/b2.png">
<img width="200" src="https://github.com/Vixiu/count_buff/blob/Buff/uncompiled/png_readme/b3.png">




