from .empleado import EmpleadoView, EmpleadoUpdateForm, EmpleadoDetallesView, empleado_view, empleado_delete_view
from .caso import CasoView, CasoUpdate, CasoDetallesView, caso_view, caso_delete_view
from .oficial import OficialView, OficialUpdate, OficialDetallesView, oficial_view, oficial_delete_view
from .repoCaso import ReporteCasoView, ReporteCasoUpdate, ReporteCasoDetallesView, reporte_caso_view, reporte_caso_delete_view
from repoServ import ReporteServicioView, ReporteServicioUpdate, ReporteServicioDetallesView, reporte_servicio_view, reporte_servicio_delete_view

from .mainPage import index

__all__ = [
    EmpleadoView, EmpleadoUpdateForm, EmpleadoDetallesView, empleado_view, empleado_delete_view,
    CasoView, CasoUpdate, CasoDetallesView, caso_view, caso_delete_view,
    OficialView, OficialUpdate, OficialDetallesView, oficial_view, oficial_delete_view,
    ReporteCasoView, ReporteCasoUpdate, ReporteCasoDetallesView, reporte_caso_view, reporte_caso_delete_view,
    ReporteServicioView, ReporteServicioUpdate, ReporteServicioDetallesView, reporte_servicio_view, reporte_servicio_delete_view
]
