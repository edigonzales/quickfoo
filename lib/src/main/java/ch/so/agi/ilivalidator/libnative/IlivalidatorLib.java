package ch.so.agi.ilivalidator.libnative;

//import java.io.File;

import org.graalvm.nativeimage.IsolateThread;
import org.graalvm.nativeimage.c.function.CEntryPoint;
import org.graalvm.nativeimage.c.type.CCharPointer;
import org.graalvm.nativeimage.c.type.CTypeConversion;
import org.interlis2.validator.Validator;

import ch.ehi.basics.logging.EhiLogger;
import ch.ehi.basics.settings.Settings;
import ch.ehi.ili2db.base.Ili2db;
import ch.ehi.ili2db.base.Ili2dbException;
import ch.ehi.ili2db.gui.Config;
import ch.ehi.ili2gpkg.GpkgMain;
//import ch.interlis.iom_j.itf.ItfReader;
//import ch.interlis.iom_j.xtf.XtfReader;
//import ch.interlis.iox.IoxEvent;
//import ch.interlis.iox.IoxException;
//import ch.interlis.iox.IoxReader;
//import ch.interlis.iox_j.EndTransferEvent;
//import ch.interlis.iox_j.StartBasketEvent;

public class IlivalidatorLib {
    
    @CEntryPoint(name = "ilivalidator")
    public static boolean validate(IsolateThread thread, CCharPointer dataFilename) {
        var settings = new Settings();
        boolean valid = Validator.runValidation(CTypeConversion.toJavaString(dataFilename), settings);
        return valid;
    }
    
    @CEntryPoint(name = "ili2gpkg")
    public static boolean ili2gpkg(IsolateThread thread, CCharPointer dataFilename) {
        Config settings = new Config();
        new GpkgMain().initConfig(settings);

        settings.setFunction(Config.FC_IMPORT);
        settings.setDoImplicitSchemaImport(true);
        
        settings.setModels("DM01AVSO24LV95");
        settings.setDefaultSrsCode("2056");
        settings.setNameOptimization(settings.NAME_OPTIMIZATION_TOPIC);
        settings.setCreateEnumDefs(Config.CREATE_ENUM_DEFS_MULTI); 

        settings.setItfTransferfile(true);

        settings.setDbfile("fubar.gpkg");
        settings.setDburl("jdbc:sqlite:" + "fubar.gpkg");
        settings.setXtffile(CTypeConversion.toJavaString(dataFilename));
        //EhiLogger.getInstance().setTraceFilter(false);
        try {
            Ili2db.run(settings, null);
        } catch (Ili2dbException e) {
            e.printStackTrace();
            return false;
        }
        
        return true;
    }

}
