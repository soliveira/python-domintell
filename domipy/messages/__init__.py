"""
:author: Thomas Delaet <thomas@delaet.org>
"""
# pylint: disable-msg=C0301
# appifo scan messages and system messages
from domipy.messages.appinfo_request import AppInfoRequest
from domipy.messages.module_info import ModuleInfoMessage
from domipy.messages.ping import Ping
from domipy.messages.hello import Hello
from domipy.messages.login_request_salt import LoginRequestSaltCommand
from domipy.messages.login_request_salt import LoginRequestSaltMessage
from domipy.messages.waiting_for_loginsw import WaitingForLoginswMessage
from domipy.messages.login_request import LoginRequest
from domipy.messages.info import InfoMessage
from domipy.messages.control import ControllMessage
from domipy.messages.session_closed import SessionClosedMessage
from domipy.messages.session_opened import SessionOpenedMessage
from domipy.messages.session_timeout import SessionTimeoutMessage
# status messages
from domipy.messages.ai_status import GenericAIStatusMessage
from domipy.messages.ao_status import GenericAOStatusMessage
from domipy.messages.do_status import GenericDOStatusMessage
from domipy.messages.di_status import GenericDIStatusMessage
from domipy.messages.dio_status import GenericDIOStatusMessage
from domipy.messages.dbir_status import DBIRStatusMessage
from domipy.messages.dmr_status import DDMRStatusMessage
from domipy.messages.ddim_status import DDIMStatusMessage
from domipy.messages.din10v_status import DIN10VStatusMessage
from domipy.messages.dism_status import DISM4StatusMessage
from domipy.messages.dism_status import DISM8StatusMessage
from domipy.messages.dmov_status import DMOVStatusMessage
from domipy.messages.dpbu_status import DPBU01StatusMessage
from domipy.messages.dpbu_status import DPBU02StatusMessage
from domipy.messages.dpbu_status import DPBU04StatusMessage
from domipy.messages.dpbu_status import DPBU06StatusMessage
from domipy.messages.dtrp_status import DTRPStatusMessage
from domipy.messages.dtrv_status import DTRVStatusMessage
from domipy.messages.dtrv_status import DTRVBTStatusMessage
from domipy.messages.dtsc_status import DTSCStatusMessage
from domipy.messages.module_status_request import ModuleStatusRequest
from domipy.messages.dled_status  import DLEDStatusMessage
# Command messages
from domipy.messages.set_ao import SetAnalogOutputMessage
from domipy.messages.set_di import DigitalShortPush
from domipy.messages.set_di import DigitalLongPush
from domipy.messages.set_di import DigitalShortPushEnd
from domipy.messages.set_di import DigitalLongPushEnd
from domipy.messages.set_dimmer import SetDimmer
from domipy.messages.set_dimmer import StartDimmer
from domipy.messages.set_dimmer import StopDimmer
from domipy.messages.set_dimmer import IncrementDimmer
from domipy.messages.set_dimmer import DecrementDimmer
from domipy.messages.set_do import SetDigitalOutputMessage
from domipy.messages.set_do import SetDigitalOutputOnMessage
from domipy.messages.set_do import SetDigitalOutputOffMessage
from domipy.messages.set_do import TogleDigitalOutputMessage
from domipy.messages.set_do import SetDigitalOutputOpenMessage
from domipy.messages.set_do import SetDigitalOutputCloseMessage
from domipy.messages.set_do import SetDigitalOutputStopMessage
from domipy.messages.set_temperature import SetTemperatureMessage
from domipy.messages.set_temperature import SetTemperatureModeMessage
from domipy.messages.set_temperature import SetTemperatureSetPointMessage
from domipy.messages.set_temperature import SetCoolingTemperatureSetPointMessage
from domipy.messages.set_temperature import SetTemperatureComfortMessage
from domipy.messages.set_temperature import SetTemperatureAutomaticMessage
from domipy.messages.set_temperature import SetTemperatureAbsenceMessage
from domipy.messages.set_temperature import SetTemperatureFrostMessage
from domipy.messages.set_temperature import SetRegulationModeMessage

from domipy.messages.temperature_status import TE1TemperaturetatusMessage
from domipy.messages.temperature_status import TE2TemperaturetatusMessage
from domipy.messages.var_status import VARStatusMessage
from domipy.messages.var_status import SYSStatusMessage
from domipy.messages.set_var import SwitchValueMessage
from domipy.messages.user_disconnected import UserDisconnected