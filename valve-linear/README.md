用于直观显示“线性度”的理论偏差。

线性度是指输入电流值I与阀杆行程y满足y = aI + b的线性关系.

但由于阀杆与电位计用直杆连接（连杆与阀杆固定、电位计端可在连杆上滑动), 将直线位移映射为转角, 故有必要考察转换之后电流值是否与电位计输出满足现行关系。

考察直线位移与转角的关系也可以证实线性度的偏差。本实验考察了在一定角度范围（体现为电位计反馈）内，阀杆直线位移的变化（体现为光栅尺反馈）.

软件输入为角度范围[theta1, theta2]，输出为两种反馈机制下的行程对比

Usage：
(under macOS)
brew install python3;
pip3 install sympy matplotlib jupyterlab;
/Users/panghuachong/Library/Python/3.8/bin/jupyter-lab &;
