# Generated from foreman_probing-0.0.2.gem by gem2rpm -*- rpm-spec -*-
# template: foreman_plugin
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name foreman_probing
%global plugin_name probing
%global foreman_min_version 1.17

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.0.4
Release: 2%{?foremandist}%{?dist}
Summary: Foreman plugin for detecting network devices
Group: Applications/Systems
License: GPLv3
URL: https://github.com/adamruzicka/foreman_probing
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: foreman >= %{foreman_min_version}
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(deface)
Requires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.9
Requires: %{?scl_prefix}rubygem(dynflow) >= 1.0
Requires: %{?scl_prefix}rubygem(dynflow) < 2
BuildRequires: foreman-plugin >= %{foreman_min_version}
BuildRequires: %{?scl_prefix}rubygem(deface)
BuildRequires: %{?scl_prefix}rubygem(foreman-tasks) >= 0.9
BuildRequires: %{?scl_prefix}rubygem(dynflow) >= 1.0
BuildRequires: %{?scl_prefix}rubygem(dynflow) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
Provides: foreman-plugin-%{plugin_name}
# end generated dependencies

%description
Foreman plugin for detecting network devices.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/config
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%posttrans
%{foreman_plugin_log}

%changelog
* Mon May 09 2022 Evgeni Golov - 0.0.4-2
- log plugin installation in posttrans

* Thu Oct 21 2021 Adam Ruzicka <aruzicka@redhat.com> 0.0.4-1
- Update to 0.0.4

* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.0.3-2
- Rebuild plugins for Ruby 2.7

* Tue Jan 21 2020 Adam Ruzicka <aruzicka@redhat.com> 0.0.3-1
- Update to 0.0.3

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.0.2-2
- Drop migrate, seed and restart posttans

* Thu Jul 19 2018 Dirk Goetz <dirk.goetz@netways.de> 0.0.2-1
- Add rubygem-foreman_probing generated by gem2rpm using the foreman_plugin template

