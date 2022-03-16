#include <controller_interface/controller.h>
#include <hardware_interface/joint_command_interface.h>
#include <pluginlib/class_list_macros.h>
// 导入创建控制器和创建命名空间的包
namespace controller_ns {
// 仅控制用 effort 界面/接口的关节
class PositionController : public controller_interface::Controller<
                               hardware_interface::EffortJointInterface> {
public:
    //创建init函数，当加载控制器管理器时会被调用
    // 在该函数中，可以从参数服务器得到所控制的关节名称，并实现实时控制
  bool init(hardware_interface::EffortJointInterface *hw, ros::NodeHandle &n) {
    std::string my_joint;
    if (!n.getParam("joint", my_joint)) {
      ROS_ERROR("Could not find joint name");
      return false;
    }

    joint_ = hw->getHandle(my_joint); // throws on failure
    return true;
  }
  // 定义传入关节的控制命令
  // 此例子里，就是error*gain的积
  // error是用目标位置减去当前位置来定义的
  void update(const ros::Time &time, const ros::Duration &period) {
    double error = setpoint_ - joint_.getPosition();
    joint_.setCommand(error * gain_);
  }
  //开启控制器
  void starting(const ros::Time &time) {}
  //关闭控制器
  void stopping(const ros::Time &time) {}
// float和double不属于积分或枚举类型，所以它们必须被声明为constexpr，或者非静态。
private:
  hardware_interface::JointHandle joint_;
  static constexpr double gain_ = 2.25;
  static constexpr double setpoint_ = 1.00;
};
// 加载特殊的marco 插入类，为了使该类动态的加载
PLUGINLIB_EXPORT_CLASS(controller_ns::PositionController,
                       controller_interface::ControllerBase);
} // namespace controller_ns