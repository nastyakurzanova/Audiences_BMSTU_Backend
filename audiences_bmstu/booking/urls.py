from django.urls import path
from .views import *

urlpatterns = [

    # path('api/pioneers/search', search_pioneers),  # GET
    # path('api/pioneers/<int:pioneer_id>/', get_pioneer_by_id),  # GET
    # path('api/audiences/search/<int:audiences_id>/', get_audiences_by_id),  # GET
    # path('api/audiences/search/', search_audiences), #в 4 лабе исчезает
    path('api/audiences/search', search_audiences),  # GET !!
    path('api/audiences/search/', search_audiences),  # GET !!
    path('api/audiences/<int:audiences_id>/', get_audiences_by_id),  # GET
    path('api/audiences/<int:audiences_id>/update/', update_audiences),  # PUT
    path('api/audiences/<int:audiences_id>/delete/', delete_audiences),  # DELETE
    path('api/audiences/create/', create_audiences),  # POST ДЕЛАЕТ ТОЛЬКО ДЕФОЛТНЫЕ 
    path('api/audiences/<int:audiences_id>/add_to_booking/', add_audiences_to_booking),  # POST добавление услуги в заявку
    path('api/audiences/<int:audiences_id>/image/', get_audiences_image),  # GET
    path('api/audiences/<int:audiences_id>/update_image/', update_audiences_image),  # PUT

    # Набор методов для заявок

    path('api/booking/search/', get_booking),  # GET
    path('api/booking/<int:booking_id>/', get_booking_by_id),  # GET
    path('api/booking/<int:booking_id>/update/', update_booking),  # PUT
    path('api/booking/<int:booking_id>/update_status_user/', update_status_user),  # PUT
    path('api/booking/<int:booking_id>/update_status_admin/', update_status_admin),  # PUT
    path('api/booking/<int:booking_id>/delete/', delete_booking),  # DELETE
    path('api/booking/<int:booking_id>/delete_audiences/<int:audiences_id>/', delete_audiences_from_booking), # DELETE

    path('api/booking/<int:booking_id>/update_free_audiences/', update_free_audiences),  # PUT

    # Набор методов для услуг
    # path('api/pioneers/search', search_pioneers),  # GET
    # path('api/pioneers/<int:pioneer_id>/', get_pioneer_by_id),  # GET
    # path('api/pioneers/<int:pioneer_id>/update/', update_pioneer),  # PUT
    # path('api/pioneers/<int:pioneer_id>/delete/', delete_pioneer),  # DELETE
    # path('api/pioneers/create/', create_pioneer),  # POST
    # path('api/pioneers/<int:pioneer_id>/add_to_discovery/', add_pioneer_to_discovery),  # POST
    # path('api/pioneers/<int:pioneer_id>/image/', get_pioneer_image),  # GET
    # path('api/pioneers/<int:pioneer_id>/update_image/', update_pioneer_image),  # PUT

    # # Набор методов для заявок
    # path('api/discoveries/search', get_discoveries),  # GET
    # path('api/discoveries/<int:discovery_id>/', get_discovery_by_id),  # GET
    # path('api/discoveries/<int:discovery_id>/update/', update_discovery),  # PUT
    # path('api/discoveries/<int:discovery_id>/update_status_user/', update_status_user),  # PUT
    # path('api/discoveries/<int:discovery_id>/update_status_admin/', update_status_admin),  # PUT
    # path('api/discoveries/<int:discovery_id>/delete/', delete_discovery),  # DELETE
    # path('api/discoveries/<int:discovery_id>/delete_pioneer/<int:pioneer_id>/', delete_pioneer_from_discovery), # DELETE
]
