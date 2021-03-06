%define mod_name contrail-openstack-dashboard
%if 0%{?_buildTag:1}
%define         _relstr      %{_buildTag}
%else
%define         _relstr      %(date -u +%y%m%d%H%M)
%endif

%define _epochstr 1

%{echo: "Building release %{_relstr}\n"}


Name:       contrail-openstack-dashboard
Epoch:      %{_epochstr}
Version:    2013.1.4
Release:    %{_relstr}
Summary:    Horizon Plugin for Contrail Neutron implementation %{?_gitVer}

Group:      Development/Libraries
License:    ASL 2.0
URL:        http://github.com/Juniper/contrail-horizon
BuildArch:  noarch

Requires:   openstack-dashboard

%description
Horizon Plugin for Contrail Neutron implementation

%build

%install

install -d -m 755 %{buildroot}%{python_sitelib}/contrail_openstack_dashboard

# Copy everything to /usr/share
cp *.py %{buildroot}%{python_sitelib}/contrail_openstack_dashboard
cp -prf openstack_dashboard %{buildroot}%{python_sitelib}/contrail_openstack_dashboard


%files -n contrail-openstack-dashboard
%dir %{python_sitelib}/contrail_openstack_dashboard
%{python_sitelib}/contrail_openstack_dashboard/*.py*
%{python_sitelib}/contrail_openstack_dashboard/openstack_dashboard

